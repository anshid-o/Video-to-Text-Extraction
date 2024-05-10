import os
from django.shortcuts import render

from django.conf import settings

from django.http import HttpResponse
from .video_text_extractor import split_video_to_images, extract_text_from_images

def index(request):
    return render(request, 'index.html')
def extract_text(request):
    if request.method == 'POST' and request.FILES['videoFile']:
        video_file = request.FILES['videoFile']
        
        # Define paths
        output_folder = 'data'
        video_path = os.path.join(output_folder, video_file.name)
        # Save video file
        if not os.path.exists(output_folder):
            print("folder created")
            os.makedirs(output_folder)
        with open(video_path, 'wb') as f:
            for chunk in video_file.chunks():
                f.write(chunk)
       
        
        # Split video into images
        split_video_to_images(video_path, output_folder)
        
        # Extract text from images
        extracted_text = extract_text_from_images(output_folder)
        
        # Save extracted text to a file (optional)
        with open('output.txt', 'w') as f:
            f.write(extracted_text)
        
        return render(request, 'result.html', {'extracted_text': extracted_text})
    
    return HttpResponse('No file selected')

def download_output_file(request):
    # Path to the output.txt file
    file_path = os.path.join(settings.BASE_DIR, 'output.txt')

    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file and read its content
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename=output.txt'
            
            return response
    else:
        return HttpResponse('File not found', status=404)