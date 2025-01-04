# Frozen Signal (900 points)

## **Description**

While hiking, Alex found on an old piece of paper, pointing to a remote Arctic location. Upon reaching the site, a strange signal can be heard, but no clear source is visible. The only clues are in the surrounding environment and the remnants of a forgotten establishment. Researching the area reveals the name of the place and other key details.<br> 
**Flag format:** Securinets{nameoftheplace,radioname,email,videosnumber,skypeid,leak,leakdate}

---

## **Solution**

### Step 1: Reverse Image Search<br>
I began by reverse searching the given image and determined that the place in question is **Greenland**.<br><br>

### Step 2: Exploring Radio Garden<br>
Using [Radio Garden](https://radio.garden/), I searched for radio stations in Greenland. This led me to the radio station **KNR**.  
Their official website can be found here: [KNR](https://knr.gl/en).<br><br>

### Step 3: Analyzing KNR's Website and YouTube Channel<br>
On the KNR website, I located their **YouTube channel**. From the channel, I gathered:<br>
- The **number of videos** they have uploaded.<br>
- Their **email address**, which is available on both the YouTube channel and the KNR website.<br><br>

### Step 4: Using the Email in OSINT Tools<br>
Using their email address, I ran a search on [Epieos](https://epieos.com/) (or a similar OSINT tool). This provided:<br>
- A **leak** associated with the email.<br>
- The **date** of the leak.<br><br>

Flag: **Securinets{knr,info@knr.gl,7383,kalaallit_nunaata_radioa,disqus.com,2012/07/01}**
