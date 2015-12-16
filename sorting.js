'use strict';
var stdin = require('get-stdin');
var postcss = require('postcss');
var sorting = require('postcss-sorting');

stdin(function (data) {
	var opts = JSON.parse(process.argv[2]);

	postcss(sorting(opts)).process(data)
	.then(function (result) {
		process.stdout.write(result.css);
	}).catch(function (err) {
		if (err.name === 'CssSyntaxError') {
			err.message += '\n' + err.showSourceCode();
		}

		console.error(err.message.replace('<css input>:', ''));
	});
});
