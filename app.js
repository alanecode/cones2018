/*
Dresses an express application with views and static files
2017. G. Szep
 */


/*global require module __dirname*/
var express = require('express');
var helpers = require('express-helpers')();
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

	// useful helper functions
	this.app.locals.link_to = helpers.link_to;
	this.app.locals.link_to_if = helpers.link_to_if;
	this.app.locals.sort_by_surname = function(a, b) {
	  	var nameA = a.surname.toUpperCase(); // ignore upper and lowercase
		  var nameB = b.surname.toUpperCase(); // ignore upper and lowercase
		  if (nameA < nameB) {
		    return -1;
		  }
		  if (nameA > nameB) {
		    return 1;
		  }

		  // names must be equal
		  return 0;
		};


}

// paths to views
App.prototype.getViews = function() {

	this.app.get('/', function(req, res) {
		res.render('pages/index');
	})

/*
Reduced complement of pages for v1.0 of site. To be reinstated when we have
more info on participants
	var staticPages = ['background', 'programme', 'registration', 'participants',
										'location', 'contact', 'feedback'];
*/
	this.app.get('/programme', function(req, res) {
		res.render('pages/programme', {
			speakers: require(__dirname + '/public/data/speakers.json')
		});

	})

	this.app.get('/attendants', function(req, res) {
		res.render('pages/attendants', {
			attendants: require(__dirname + '/public/data/attendants.json')
		});

	})

	var staticPages = ['background', 'registration', 'location', 'contact'];

	staticPages.forEach(function(page) {
		this.app.get('/' + page, function(req, res) {
			res.render('pages/' + page);
		})
	}, this); // specify context within forEach loop

}
