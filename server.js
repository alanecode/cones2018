/*
Module initialising server with site
2017. G. Szep
*/

/*eslint no-console: ["error", { allow: ["log"] }] */
/*global require */

// serve app with views and static files
console.log('[Node] Configuring Application')
const App = require('./app'),
	app = new App()

// setup realtime i/o on socket
const server = require('http').Server(app)
server.listen(8000)
console.log('[Node] HTTP Server Listening')
