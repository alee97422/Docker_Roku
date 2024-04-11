# Docker_Roku


simple roku remote using python streamlit and requests is light weight and opens in your browser

what you need:
docker installed 
IP address of the roku devices you want to use ( this can be found in your phones roku app)


to run use this remote

1. clone this repo 

```
git clone https://github.com/alee97422/Docker_Roku.git
cd Docker_roku

```
2. edit the app.py file to include your personal roku IP addresses

  ```

# Define the Roku devices with their IP addresses
5   │ roku_devices = {
6   │     "Bedroom": "192.168.1.ZZZ", # Replace ZZZ with the actual IP address
7   │     "Children's Room": "192.168.1.XXX",  # Replace XXX with the actual IP address
8   │     "Living Room": "192.168.1.YYY"  # Replace YYY with the actual IP address
9   │ }

  ```

3. build container 

```

docker build -t roku_remote .

```

4. run container exposing port 8501
   ```
  
   docker run -p 8501:8501 roku_remote:latest

   ```

5. the output will be use either ctrl+mouseclick on the link or copy and paste to your browser 

```

╰─λ docker run -p 8501:8501 roku_remote:latest

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.


You can now view your Streamlit app in your browser.

URL: http://0.0.0.0:8501

```


Using it is super simple just select your roku device from the drop down and send commands as such 

Feel free to modify this to make it easier for your use case 

in the future id like to add:
channel button options
quick command buttons instead of drop down ( play/pause, FF, Rewind, Home)








   
