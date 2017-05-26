var app = angular.module("rfDashboard", []);

app.filter('refreshSort', function() {

	function refreshOrder(item) {

        switch(item) {
            case 'Failed':
                return 1;

            case 'Delayed':
                return 2;

            case 'Successful':
                return 3;
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

		console.log(filtered);
	    return filtered;
	    
  	};

});