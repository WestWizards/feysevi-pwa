import React from "react"
import {Layout} from "antd"
import {Route} from "react-router-dom"
import Home from './components/Home'

import logo from "./logo.svg"
import "./App.css"

class App extends React.Component {
	render() {
		return (
				<Layout className="App">
					<Layout.Header className="App-header">
						<img src={logo} className="App-logo" alt="logo"/>
						<h1 className="App-title">FèySèvi</h1>
					</Layout.Header>
					<Layout.Content>
						<Route exact path="/" component={Home} />
					</Layout.Content>
					<Layout.Footer>
						FèySèvi © − 2018 Tous droits réservés
					</Layout.Footer>
				</Layout>
		)
	}
}

export default App
