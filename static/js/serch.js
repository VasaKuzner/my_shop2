// In your Javascript (external .js resource or <script> tag)


//  загрузка ввідділень

function loadWarehouses() {
    var selectedSettlement = $('#id_address').val();
    console.log(selectedSettlement)

    if (selectedSettlement !== "") {
        $.ajax({
            url: 'https://api.novaposhta.ua/v2.0/json/',
            method: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                "apiKey": "86d1f8ea6e378564cde4337f24dda1c2",
                "modelName": "Address",
                "calledMethod": "getWarehouses",
                "methodProperties": {
                    "SettlementRef": selectedSettlement,
                    "Limit": 100
                }
            }),
            success: function(response) {
                var warehouses = response.data;
                var warehouseSelect = $('#id_adres_past');
                warehouseSelect.empty();
                warehouseSelect.append($('<option>', {
                    value: "" ,
                    text: "--- Виберіть відділення ---",

                }));
                $.each(warehouses, function(i, warehouse) {
                    warehouseSelect.append($('<option >', {
                        value: warehouse.CityDescription,
                        text: warehouse.Description,

                    }));
                });
            },
            error: function(response) {
                //console.log(response);
            }
        });
    }
}



// Все старе що я ранше робив
//window.onload = function() {
//loadjblast();
//};
//// загрузка Областей
//function loadjblast () {
//    $.ajax({
//        url: 'https://api.novaposhta.ua/v2.0/json/',
//        method: 'POST',
//        dataType: 'json',
//        data: JSON.stringify({
//            "apiKey": "86d1f8ea6e378564cde4337f24dda1c2",
//            "modelName": "Address",
//            "calledMethod": "getSettlementAreas",
//            "methodProperties": {
//          }
//
//        }),
//
//
//        success: function(response) {
//            var settlements = response.data;
//            var settlementSelect = $('#id_state');
//            settlementSelect.empty();
//            settlementSelect.append($('<option>', {
//               value: "",
//                text: "--- Виберіть область  ---",
//
//            }));
//            $.each(settlements, function(i, settlement) {
//                settlementSelect.append($('<option>', {
//                    value: settlement.Ref,
//                    text: settlement.Description ,
//                }));
//
//            });
//        },
//        error: function(response) {
//            console.error(response);
//        }
//    });
//}
////  Загрузка районів
//
//function loadCityRegion() {
//    var selectedArea = $('#id_state').val();
//
////      console.log(selectedArea)
//    if (selectedArea !== "") {
//        $.ajax({
//            url: 'https://api.novaposhta.ua/v2.0/json/',
//            method: 'POST',
//            dataType: 'json',
//            data: JSON.stringify({
//                "apiKey": "86d1f8ea6e378564cde4337f24dda1c2",
//                "modelName": "Address",
//                "calledMethod": "getSettlementCountryRegion",
//                "methodProperties": {
//                   "AreaRef": selectedArea,
//                }
//            }),
//            success: function(response) {
//                var settlements = response.data;
//                var settlementSelect = $('#id_city_region');
//                settlementSelect.empty();
//                settlementSelect.append($('<option>', {
//                    value: "",
//                    text: "--- Виберіть район ---"
//
//                }));
//
//                $.each(settlements, function(i, settlement) {
//
//                    settlementSelect.append($('<option>', {
//                        value: settlement.Ref ,
//                        text: settlement.Description
//
//                    }));
//                });
//            },
//            error: function(response) {
//                //console.log(response);
//            }
//        });
//    }
//}
//
//// Загрузка населених пунктів
//
//
//
//function loadCity() {
//    var selectedArea = $('#id_city_region').val();
////    var refregion = $('#id_city_region').val();
//
//    if (selectedArea !== "") {
//        $.ajax({
//            url: 'https://api.novaposhta.ua/v2.0/json/',
//            method: 'POST',
//            dataType: 'json',
//            data: JSON.stringify({
//                "apiKey": "86d1f8ea6e378564cde4337f24dda1c2",
//                "modelName": "Address",
//                "calledMethod": "getSettlements",
//                "methodProperties": {
//                   "RegionRef": selectedArea,
//                }
//            }),
//            success: function(response) {
//                var settlements = response.data;
//                var settlementSelect = $('#id_city');
//                settlementSelect.empty();
//                settlementSelect.append($('<option>', {
//                    value: "",
//                    text: "--- Виберіть населений пункт ---"
//                }));
//                $.each(settlements, function(i, settlement) {
//
//                    settlementSelect.append($('<option>', {
//                        value: settlement.Ref ,
//                        text: settlement.Description,
//
//                    }));
////                    option.attr('data-ref', settlement.Ref); // Додайте атрибут data-ref
////                    settlementSelect.append(option);
//
//                });
//            },
//            error: function(response) {
//                //console.log(response);
//            }
//        });
//    }
//}





