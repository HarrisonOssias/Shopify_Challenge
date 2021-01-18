# Shopify_Challenge
Hello :) This is my submission for the Shopify Backend Challenge, part of my application to the Backend and SRE internship roles at Shopify for the summer of 2020. 

I chose to make two mini "apps" that both use a Python/Flask backend and HTML/CSS frontend. I didnt know whether to create a image file upload/download app with other functionalities or to actually create a repository of DOCKER IMAGES.  Pretty funny right! So I created two mini applications that have both been dockerized.  

## Image Loader
I created this app to help upload and download images files (jpeg, png, etc..).  It uses Flask-Upload to find local directories. 

*How to Run*
Either use Docker build and Docker Run -p 4000:4000 <testname> in the main directory (image_loader) or cd into loader_app run: 'pipenv shell' and 'flask run' 

## Sort-Compare
Next,I made sort-compare which is a dockerized application to sort a given array and compare the runtimes of quick, merge, and bubble sort.

*How to Run*
Either use Docker build and Docker Run -p 4000:4000 <testname> in the main directory (image_loader) or cd into loader_app run: 'pipenv shell' and 'flask run' 


Thank you so much for your time. I had a lot of fun making this for you :) 
