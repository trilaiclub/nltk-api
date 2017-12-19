'use strict';
var exec = require('sync-exec');

module.exports = function(Service) {
    Service.result = [];
    Service.process = function(name, inputJson, cb) {
        Service.result = [];
        var exeName = process.cwd() + "/client/" + name
        for(var i = 0; i < inputJson.length; i++) {
            var output = exec(exeName + ' ' + inputJson[i]);
            Service.result.push(output.stdout.trim());
        }
        cb(null, Service.result);
    }

    Service.execute = function(exeName, input, cb) {
        var child = exec(exeName + " " + input, (error, stdout, stderr) => {
            Service.result.push(stdout);
        });
    }
    Service.remoteMethod(
        'process', {
          accepts:  [
              {arg: 'name', type: 'string', required: true},
              {arg: 'inputJson', type: 'array', required: true}
            ],
          returns: {arg: 'output', type: 'array'}
    });
};
