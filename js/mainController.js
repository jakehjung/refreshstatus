app.controller("rfController", ['$scope', '$http', '$timeout', '$interval', function ($scope, $http, $timeout, $interval) {
	
	// $scope.displayData = function () {

	// 	$http.get('db.php').success(function(data) {
	//     	$scope.refreshes = data;
	//     	console.log(data);
	//     });
	    

	// 	$timeout(function() {
	//     	$scope.displayData();
	//     },300000)

	// };

	// $scope.modalopen = angular.element('body').hasClass('modal-open');

	$scope.timer = null;

	$scope.displayData = function () {

		$http.get('db.php').success(function(data) {
	    	$scope.refreshes = data;
	    });
	
	};

	$scope.startTimer = function() {
		$scope.timer = $interval(function() {
			$scope.displayData();
		}, 1000)
	}

	$scope.stopTimer = function() {
		if(angular.isDefined($scope.timer)) {
			$interval.cancel($scope.timer);
		}
	}


	// setInterval(function() {
	// 	if($scope.runInterval){
 //            $scope.displayData();
 //            console.log("Done");
 //        }
	// },1000)

	

	// $scope.renewData = function() {

	// 	if (!$("#rfmodal0").data('bs.modal').isShown) {
	// 		$timeout(function() {
	// 	    	$scope.displayData();
	// 	    },10000)
	//     }

	// }

	

	
}]);