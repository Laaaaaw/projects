
var Connection = require('tedious').Connection;  
    var config = {  
        server: 'galletas99.mysql.pythonanywhere-services.com',
        authentication: {
            type: 'default',
            options: {
                userName: 'galletas99',
                password: 'kokalol88'
            }
        },
        options: {
            // If you are on Microsoft Azure, you need encryption:
            encrypt: true,
            database: 'galletas99$OnlineShop'
        }
    };  
    var connection = new Connection(config);  
    connection.on('connect', function(err) {  
        // If no error, then good to proceed.
        console.log("Connected");  
    });
    
    connection.connect();
