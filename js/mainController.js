app.controller('modalController', function ($scope, $modalInstance, refresh) {

	$scope.refresh = refresh;

});

app.controller("rfController", ['$scope', function ($scope, $timeout, $modal, $log) {

	$scope.refreshes = [
		{
			company: "Pitney",
			status: "Successful",
			comment: "Hello"
		},
		{	
			company: "Honeywell",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "Box",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "Flexera",
			status: "Failed",
			comment: "Hello2"
		},
		{
			company: "Cisco",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "NCR",
			status: "Delayed",
			comment: "Hello2"
		},
		{
			company: "Aderant",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "Broadridge",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "Datrium",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "EMC",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "FONA",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "Gigamon",
			status: "Delayed",
			comment: "Hello2"
		},
		{
			company: "HoneywellSafetyandProductivitySolutions",
			status: "Failed",
			comment: "Hello2"
		},
		{
			company: "PureStorageInc",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "RSA",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "ServiceMax",
			status: "Delayed",
			comment: "Hello2"
		},
		{
			company: "ThomsonReuters",
			status: "Successful",
			comment: "Hello2"
		},
		{
			company: "Sohee's Company",
			status: "Delayed"
		}
	];

	// MODAL WINDOW
	$scope.open = function (_refresh) {

        var modalInstance = $modal.open({
			controller: "modalController",
			templateUrl: "refreshContent.html",
			resolve: {
				refresh: function() {
			    	return _refresh;
				}
			}
        });

    };

}]);