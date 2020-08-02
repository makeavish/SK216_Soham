import React, {useState} from 'react'

const Home = () =>{
    const [search, setSearchValue] = useState("")
    const PostData = () =>{
        if(search){
            console.log(search)
            return
        }
    }
    return(
        <div>
            <div className= "content">
                <div className= "brand-header">
                    <h1>Cyber Abuse Revelation Engine</h1>
                </div>

                    <label htmlFor= "options">Select Search Type</label>
                    <select multiple id= "options" className="browser-default">
                        <option value="DEFAULT">All</option>
                        <option value="1">Text</option>
                        <option value="2">Image</option>
                        <option value="3">Audio</option>
                    </select>

                <div className="input-field">
                    <i className="material-icons prefix">search</i>


                    <input id="search"
                     type="text" 
                     value= {search}
                     onChange= {(event) => setSearchValue(event.target.value)}
                     />
                    <label htmlFor="search">Search</label>

                    <button className="btn waves-effect waves-light" type="submit" name="action"
                    onClick= {() => PostData()}>
                        Submit
                    </button>
                </div>
            </div>
        </div>
    )
}

export default Home;


