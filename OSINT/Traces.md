# Traces (800 points)

## **Description**

Baboucha, obsessed with planes, showed me a photo on a site where comments exploded. Among them, one uploader—always posting photos—mentioned “the leaves” and left squawk remarks. They once dropped a clue about a Boeing 737 MAX, linked to a factory. What’s the catch?<br><br>
<br> 
**Flag format:** Securinets{PlaneName_UserName_YearsOfMembership_postDate_ordersNumber_FactoryName_FactoryLocation}

---

## **Solution**

This challenge required reverse image searching, analyzing comments, and extracting information from posts on FlightAware.<br><br>

### Step 1: Reverse Image Search<br>
I began by performing a reverse image search on the plane's image. The search revealed that the manufacturer is **Boeing**, specifically the **Boeing 787**.<br><br>

### Step 2: Searching on FlightAware<br>
Using the information about the Boeing 787, I searched for it on [FlightAware](https://www.flightaware.com/) under the community page. There, I found the same image of the plane and discovered a comment by [**Mark Thomas**](https://www.flightaware.com/user/mpmt06/), who mentioned **the leaves**. This comment provided the following clues:<br>
- **Mark Thomas' membership years**<br>
- His **username**<br><br>

### Step 3: Investigating Mark Thomas' Squawk<br>
I checked [Mark Thomas' squawk comments](https://www.flightaware.com/user/mpmt06/squawkcomments/page/3) and navigated to the **third page**. On this page, I found a post mentioning:<br>
- The **Boeing 737 MAX**<br>
- Its **date**<br>
- Its **order numbers**<br><br>

### Step 4: Identifying the Factory Name<br>
Using the information from the post (date, orders, and Boeing 737 MAX), I performed a quick Google search. This revealed the name of the factory where the aircraft is manufactured.<br><br>

Flag: **Securinets{7_august}**
