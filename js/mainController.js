app.controller("rfController", ['$scope', '$http', '$timeout', '$interval', '$window', function ($scope, $http, $timeout, $interval, $window) {
	
	$scope.timer = null;

	$scope.displayData = function () {

		$http.get('db.php').success(function(data) {
	    	$scope.refreshes = data;
	    	console.log("displayData was called!");
	    });
	
	};

	$scope.startTimer = function() {
		$scope.timer = $interval(function() {
			$scope.displayData();
		}, 2000)
	}

	$scope.stopTimer = function() {
		if(angular.isDefined($scope.timer)) {
			$interval.cancel($scope.timer);
		}
	}

	$scope.deleteNode = function(index) {
		var orgId_r = angular.element(document.getElementsByClassName("orgid"));
		var orgid = orgId_r[index].attributes['value'].value;
		var confirmDelete = $window.confirm('Are you sure you want to delete?');

		if(confirmDelete) {
			$http.get('delete.php?orgid=' + orgid).success(function() {
				$window.location.reload();
			});
		}
	}
	
}]);