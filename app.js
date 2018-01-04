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
		res.render('pages/index')
	})

	this.app.get('/background', function(req, res) {
		res.render('pages/background')
	})

	this.app.get('/programme', function(req, res) {
		res.render('pages/programme')
	})

	this.app.get('/registration', function(req, res) {
		res.render('pages/registration')
	})

	this.app.get('/participants', function(req, res) {
		res.render('pages/participants')
	})

	this.app.get('/accommodation', function(req, res) {
		res.render('pages/accommodation')
	})

	this.app.get('/contact', function(req, res) {
		res.render('pages/contact')
	})

	this.app.get('/feedback', function(req, res) {
		res.render('pages/feedback')
	})
}
