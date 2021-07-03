payload = {
         "customerDetails" : {
         "soldToCustomerNumber" : "5000871",
         "billToCustomerNumber" : "",
         "includeBasicFloorplans" : "FALSE",
         "vehicleAttributes" : [ {
         "vehicleReferenceId" : "7037088",
         "vehicleYear" : "2018",
         "maxOdometerReading" : "120",
         "asIsIndicator" : "FALSE",
         "totalVehicleDebitAmount" : "1000",
         "salvageUnitIndicator" : "FALSE",
         "salesChannel" : "RMS",
         "vehicleType" : "V",
         "saleType" : "O",
         "hondaFloorplanThresholdFlag" : "TRUE",
         "sellerAccount" : ""
         }
         ]
         }
         }
print(payload.keys())


L=payload["customerDetails"]["vehicleAttributes"]

print(L[0]["vehicleReferenceId"])

print(payload["customerDetails"]["vehicleAttributes"][0]["maxOdometerReading"])

L1=payload["customerDetails"]["soldToCustomerNumber"]
print(L1)