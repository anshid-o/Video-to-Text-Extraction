<h1>Video-to-Text-Extraction</h1>

<p>
  <strong>Video-to-Text-Extraction</strong> is a web application that allows users to extract text from video frames. Built using Django, the application utilizes the Tesseract OCR (Optical Character Recognition) Python library to process video files and convert the content of video frames into readable text.
</p>

<h2>Features</h2>
<ul>
  <li><strong>Video Upload:</strong> Users can upload video files in various formats.</li>
  <li><strong>Frame Extraction:</strong> The application extracts frames from the video at specified intervals.</li>
  <li><strong>Text Extraction:</strong> Using Tesseract OCR, the application processes each frame to extract any text present.</li>
  <li><strong>Downloadable Results:</strong> The extracted text can be downloaded as a text file for further use.</li>
  <li><strong>User-Friendly Interface:</strong> The website offers a clean and intuitive UI, making it easy to upload videos and view extraction results.</li>
  <li><strong>Django Admin Interface:</strong> Manage users and uploaded videos through the Django admin interface.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
  <li><strong>Django:</strong> The back-end framework used to build the web application.</li>
  <li><strong>Tesseract OCR:</strong> A powerful OCR library for extracting text from images.</li>
  <li><strong>Python:</strong> The programming language used for implementing the application logic.</li>
  <li><strong>OpenCV:</strong> Utilized for video processing and frame extraction.</li>
  <li><strong>HTML/CSS:</strong> For building the front-end user interface.</li>
  <li><strong>Bootstrap:</strong> Used for responsive and modern web design.</li>
  <li><strong>SQLite:</strong> The default database for managing video data and extraction results.</li>
</ul>

<h2>Getting Started</h2>
<ol>
  <li>Clone the repository to your local machine.</li>
  <li>Ensure you have Python and Django installed.</li>
  <li>Install the required Python packages using <code>pip install -r requirements.txt</code>.</li>
  <li>Configure Tesseract OCR by installing it on your system and ensuring it's accessible via the command line.</li>
  <li>Run <code>python manage.py migrate</code> to set up the database.</li>
  <li>Start the Django development server with <code>python manage.py runserver</code>.</li>
  <li>Access the application by navigating to <a href="http://localhost:8000">http://localhost:8000</a> in your web browser.</li>
</ol>

<h2>Contributing</h2>
<p>
  Contributions are welcome! If you have any suggestions, improvements, or find any issues, feel free to submit a pull request or open an issue on the GitHub repository.
</p>

<h2>License</h2>
<p>
  This project is licensed under the <strong>MIT License</strong> - see the <a href="LICENSE">LICENSE</a> file for details.
</p>

