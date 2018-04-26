import React, {Component} from 'react';
import "./index.css"
class Intro extends Component {
    render()    {
        this.hi = 'I have a soft comforter which you might like';
        return (
            <div class="head_top">
                <div1>Hello from the header<br /></div1>
                <div2>Do you like rainbows?<br /></div2>
                <div3>I do too<br /></div3>
                <div4>It's been lonely, here in the Intro...<br /></div4>
                <div5>Do you want to grab lunch at some point?<br /></div5>
                <div6>I think we can find company in each other<br /></div6>
                <div7>{this.hi}</div7>

            </div>
        );
    }
}

export default Intro;