# Wifi-remote-control
Too many Wifi-devices. Made one master switch to rule them all.

Kauko.py: ESP-01 reads nine buttons via CD4014 parallel-to-serial and creates web-page
where ON:{X} and OFF:{X} signals appear. Long press is the OFF. Deep-sleeps after 30 seconds. Will work
for years with two regular AA-batteries. White button is a power switch and it takes 5 seconds to create a Wifi-connection, but you can get used to that.

Kaukosaadin: Bash-script polls the web-page from above and interprets them as needed.
Great innovation is the number 9 button, which just turns everything off.

<img src=saadin.png>

<img src=napit.png>
