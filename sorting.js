'use strict';
var getStdin = require('get-stdin');
var postcss = require('postcss');
var scss = require('postcss-scss');
var sorting = require('postcss-sorting');

getStdin().then(function (data) {
	var opts = JSON.parse(process.argv[2]);

	postcss(sorting(opts)).process(data, { syntax: scss, from: undefined })
	.then(function (result) {
		process.stdout.write(result.css);
	}).catch(function (err) {
		if (err.name === 'CssSyntaxError') {
			err.message += '\n' + err.showSourceCode();
		}

		console.error(err.message.replace('<css input>:', ''));
	});
});
