import React from "react"
import {render} from "react-snapshot"
import {Provider} from "react-redux"
import {Route} from "react-router-dom"
import {ConnectedRouter} from "react-router-redux"
import {Login, Signup} from "./components"
import store, {history} from "./store"
import App from "./App"
import registerServiceWorker from "./registerServiceWorker"

import "./index.css"


render(
		<Provider store={store}>
			<ConnectedRouter history={history}>
				<div>
					<Route exact path="/" component={App}/>
					<Route exact path="/login" component={Login}/>
					<Route exact path="/signup" component={Signup}/>
				</div>
			</ConnectedRouter>
		</Provider>, document.getElementById("root"))

registerServiceWorker()
