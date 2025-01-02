# Task: Lost in the Logs

## Description
> Found this peculiar file with strange data.  
> Can you figure out what it holds?

> Author: ADX2K

The challenge provides a web request log file that contains a mix of HTTP response codes. Your goal is to uncover the flag hidden within the `200 OK` responses.

---

## Solution

### Step 1: Analyze the Log File
The log file contains multiple HTTP requests and their respective responses, such as `404 Not Found` and `200 OK`. <br>
The flag is hidden in the `200 OK` responses.


### Step 2: Filter the `200 OK` Responses
Manually inspecting the file for lines with `200 OK` can work, but automating the process is more efficient. Use the following command to filter the `200 OK` responses:

```strings server.log | grep 200```<br>
<div align="center">
  <img src="200 Respond.png" alt="200 Respond">
</div>
Here we go i think we got the 2 parts of the flag but they seem encoded in base64 :<br><br>
Encoded Flag : <br>

``U2VjdXJpbmV0c3tMMGdfRjFsM3NfNHIzXzFtcDBydDRudH0=``

### Step 3: Decode the flag 
```echo "U2VjdXJpbmV0c3tMMGdfRjFsM3NfNHIzXzFtcDBydDRudH0=" | base64 -d```

Good job, Flag : ```Securinets{L0g_F1l3s_4r3_1mp0rt4nt}```
