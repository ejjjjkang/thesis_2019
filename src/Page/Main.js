
import React, { Component } from "react";
import d3 from "d3";
import './Main.scss'

// import Video from "./Video";

export class Main extends React.Component {

    componentDidMount(){
   
          
          
    }

    

    
    render() {
        const element = (
            <ul class="bg-bubbles">
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
            </ul>
          );
        return(
            <div>
            <div className ="Name_area">PROJECT GODOT</div>
            <div className="Main_Wrapper">
                <div className="video_wrapper">
            {/* <Video></Video> */}
                {element}
          
                </div>
            </div>

            </div>
        )
    }
}

export default Main;