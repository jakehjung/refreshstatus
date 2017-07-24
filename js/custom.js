var app = angular.module("rfDashboard", []);

app.filter('refreshSort', function() {

	function refreshOrder(item) {

        switch(item) {
            case 'Failed':
                return 1;

            case 'Delayed':
                return 2;

            case 'Started':
                return 3;

            case 'Successful':
                return 4;
        }

    };

    return function(items, field) {

    	var filtered = [];

	    angular.forEach(items, function(item) {
	    	filtered.push(item);
	    });

	    filtered.sort(function (a, b) {
	    	return (refreshOrder(a.status) > refreshOrder(b.status) ? 1 : -1);
	    });

	    return filtered;
	    
  	};

});