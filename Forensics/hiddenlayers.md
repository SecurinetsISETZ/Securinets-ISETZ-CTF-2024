


**Flag format:** `Securinets{ _ }`  

---

**Flag:** `Securinets{Hex_3s_The_solution}`  

---

###  Hidden Layers in an Image
This challenge also involves a photo that contains another hidden image embedded within its hexadecimal content.
![Description](Forensics/chal.png)
#### Steps to Solve:
1. Analyze the image file for metadata using the `exiftool` command:
   ```bash
   exiftool photo.png
   exiftool -all photo.png
   exiftool -b -EmbeddedFile photo.png > extracted_file
