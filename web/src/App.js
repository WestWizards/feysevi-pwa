import React from "react"
import Helmet from "react-helmet"
import {Layout} from "antd"
import {Route} from "react-router-dom"
import {Home, Footer, Login, Signup} from "./components"

import logo from "./logo.svg"
import "./App.css"

class App extends React.Component {
	render() {
		return (
				<Layout className="App">
					<Helmet title="FèySèvi - Louez ou Louez !"/>
					<Layout.Header className="App-header">
						<h1 className="App-title" style={{color: "white"}}>FèySèvi</h1>
					</Layout.Header>
					<Layout.Content>
						<Route exact path="/" component={Home}/>
					</Layout.Content>
					<Footer/>
				</Layout>
		)
	}
}

export default App
