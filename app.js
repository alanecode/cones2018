/*
Dresses an express application with views and static files
2017. G. Szep
 */

/*global require module __dirname*/
var express = require('express')
var App = module.exports = function() {

	// initialise express app
	this.app = express()
	this.initialise()
	this.getViews()

	// return dressed app
	return this.app
}

// serve static files and use templating system
App.prototype.initialise = function() {

	this.app.use(express.static(__dirname + '/public'))
	this.app.set('view engine', 'ejs')
}

// paths to views
App.prototype.getViews = function() {

	this.app.get('/', function(req, res) {
		res.render('pages/index');
	})

<<<<<<< 083f92e3b6b754f27fadf7849607c8328b6f418e
/*
Reduced complement of pages for v1.0 of site. To be reinstated when we have
more info on participants
	var staticPages = ['background', 'programme', 'registration', 'participants',
										'location', 'contact', 'feedback'];
*/
var staticPages = ['background', 'registration', 'location', 'contact'];
=======
	this.app.get('/speakers', function(req, res) {
		res.render('pages/speakers', {
			speakers: require(__dirname + '/public/data/speakers.json')
		});

	})

	this.app.get('/attendants', function(req, res) {
		res.render('pages/attendants', {
			attendants: require(__dirname + '/public/data/attendants.json')
		});

	})

	var staticPages = ['background', 'registration', 'accommodation',
		'contact', 'feedback'];
>>>>>>> Load attendants and speakers into template.

	staticPages.forEach(function(page) {
		this.app.get('/' + page, function(req, res) {
			res.render('pages/' + page);
		})
	}, this); // specify context within forEach loop

}
