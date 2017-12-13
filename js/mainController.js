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

	$scope.getStatus = function() {

	}

	// Delete node
	$scope.deleteNode = function(index) {
		var orgid_r = angular.element(document.getElementsByClassName("orgid"));
		var orgid = orgid_r[index].attributes['value'].value;
		var confirmDelete = $window.confirm('Are you sure you want to delete?');

		if(confirmDelete) {
			$http.get('delete.php?orgid=' + orgid).success(function() {
				$window.location.reload();
			});
		}
	}

	$scope.getStatus = function(index) {
		var e = document.getElementById(index);
		var selected = e.options[e.selectedIndex].value;

		return selected;
	}
	
	$scope.editNode = function(index) {
		var orgid_r = angular.element(document.getElementsByClassName("orgid"));
		var orgid = orgid_r[index].attributes['value'].value;
		var status_r = angular.element(document.getElementsByClassName("status"));
		var status = $scope.getStatus(index);
		var confirmEdit = $window.confirm('Are you sure you want to submit the change?');

		if(confirmEdit) {
			$http.get('edit.php?status=' + status + '&orgid=' + orgid).success(function(data) {
				$window.location.reload();
			});
		}

	}
	
}]);