# python_sms_tool
SMS sending tool using python, selenium and free sms sending gateway(160by2.com)


This program uses Selenium webdriver to automate the sms sending process.
Selenium, Chrome and chromedriver should be installed.<br><br>
  <b>To install Selenium:</b>pip install selenium <br>
  <b>To install chrome:</b> https://www.google.com/chrome/browser/desktop/index.html<br>
  <b>To install Chromedriver:</b> https://chromedriver.storage.googleapis.com/index.html?path=2.39/<br><br>
Clone this repo and import SMS in your code:<br>
After importing:<br>
<b>Write the following in your code:<b><br>
	
sms= SMS("http://www.160by2.com")<br>
sms.get_access()<br>
sms.login(username, password)<br>
sms.send(phone_no, message)<br>
sms.browser_quit()
