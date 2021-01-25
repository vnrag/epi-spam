# epi-spam

**Goal:**
This project should receive responses from users that want to flag their Epi newsletter as spam and report it to Epi database.

**Description:**
Users are sent an email to fill a form if they want to stop receiving newsletter and why they consider it as spam. The response is then processed and sent using Episerver Campaign REST API to be logged. Otherwise if users flag the newsletter as spam using their email provider it is not reported to VNR.
