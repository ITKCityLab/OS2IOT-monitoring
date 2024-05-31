# Setup
1. Rename `settings.EXAMPLE.json` to `settings.json`
2. Edit `settings.json` to reflect your organisation
3. Run `python3 ./gateways.py` to confirm that it works
4. Create an hourly task: This can be done using Windows' task scheduler or issuing `crontab -e` and inserting a line like `55 * * * * python3.12 /path/OS2IoT-monitoring/gateways.py`


# License
 This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

Good luck!

- Kristian Risager Larsen, [IoT Lab, Aarhus Kommune](https://iot.aarhus.dk)