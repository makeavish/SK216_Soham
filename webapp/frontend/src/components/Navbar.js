import React from 'react'
import {Link} from 'react-router-dom'

const Navbar = ()=>{
    return (
        <div>
            <nav>
                <div className="nav-wrapper black">
                    <Link to="/" className="brand-logo left"><i className="material-icons">adb</i>CARE</Link>
                    {/* <ul id="nav-mobile" className="right">
                        <li><Link to="\">Sass</Link></li>
                        <li><Link to="\">Components</Link></li>
                        <li><Link to="\">JavaScript</Link></li>
                    </ul> */}
                    <ul id="nav-original" className="right">
                        <li><Link className="nav-items" to="/test_results">Test Results</Link></li>
                        <li><Link className="nav-items" to="/forums">Forums</Link></li>
                        <li><Link className="nav-items" to="/login">Logout</Link></li>
                    </ul>
                </div>
            </nav>
            <div className= "body">
                <div className= "background-image">
                </div>
            </div>
        </div>
    )
}

export default Navbar;