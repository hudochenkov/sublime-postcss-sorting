const getStdin = require('get-stdin');
const postcss = require('postcss');
const scss = require('postcss-scss');
const sorting = require('postcss-sorting');

getStdin().then(data => {
	const opts = JSON.parse(process.argv[2]);

	postcss(sorting(opts))
		.process(data, {
			syntax: scss,
			from: undefined,
		})
		.then(result => {
			process.stdout.write(result.css);
		})
		.catch(err => {
			if (err.name === 'CssSyntaxError') {
				err.message += `\n${err.showSourceCode()}`;
			}

			console.error(err.message.replace('<css input>:', ''));
		});
});
