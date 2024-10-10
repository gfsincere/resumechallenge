import os

class ImageGallery:
    def __init__(self, path):
        self.folder_path = folder_path
        self.div_class = "gallery-item"
        self.image_extensions = {".jpg", ".jpeg", ".png"}

    def get_images(self):
        return [
            img for img in os.listdir(self.folder_path)
            if os.path.splitext(img)[1].lower() in self.image_extensions
        ]

    def generate_gallery_html(self):
        gallery_html = ""
        images = self.get_images()
    
        for img in images:
            image_path = os.path.join(self.folder_path, image)
            gallery_html += f'<div class="{self.div_class}">'
            gallery_html += f'<img src="{image_path}" alt="{image}" />'
            gallery_html += "</div>"

        return gallery_html

def insert_gallery_html(self, existing_html, output_html):
    with open(existing_html, "r") as f:
        html_content = f.read()

    gallery_html = self.generate_gallery_html()

# Replace placeholder with gallery html content
    updated_html = html_content.replace("<!-- gallery-placeholder -->", gallery_html)

    # Write updated html content to output file
    with open(output_html, "w") as f:
        f.write(updated_html)

    print(f"Gallery HTML inserted into {output_html}")

gallery = ImageGallery("/static/theme/assets/img")
gallery.insert_gallery_html("resumechall/apps/public/templates/photos.html", "resumechall/apps/public/templates/photos.html")




    