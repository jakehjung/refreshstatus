app.controller("rfController", ['$scope', '$http', '$timeout', function ($scope, $http, $timeout) {

	$scope.displayData = function () {

		$http.get('db.php').success(function(data) {
	    	$scope.refreshes = data;
	    	console.log(data);
	    });
	    
		$timeout(function() {
	    	$scope.displayData();
	    },10000)
	    
		// $scope.renewData();

	};

	// $scope.renewData = function() {

	// 	if (!$("#rfmodal0").data('bs.modal').isShown) {
	// 		$timeout(function() {
	// 	    	$scope.displayData();
	// 	    },10000)
	//     }

	// }

	

	
}]);
















