# payment-service
### The service consists of one page with the following elements:
* The amount of payment (input field of the sum);
* Payment currency (drop-down list with values ​​of EUR, USD, RUB);
* Product description (multi-line information entry field);
* Submit (button);
### When you click on the "Submit" button, the following happens:
* If the currency in the drop-down list is "EUR", the user is sent to the payment page without selecting the direction.
* If the currency specifies "USD", then an invoice is requested to pay for payment on the API in the Piastrix currency. If a correct answer is received, the user is redirected to the PiaStrix payment system payment page (on the URL from the answer).
* If the currency is specified by "RUB", then a request is requested to pay for payment by API. If a correct answer is received, the user must redirect to the AdvCash payment system payment page. 
