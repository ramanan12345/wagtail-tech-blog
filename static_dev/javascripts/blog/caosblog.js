/*****
 * TABLE OF CONTENTS
 *
 * React Navigation
 *    - Mixins
 *    - Components
 *    - Navigation Classes
 *    - Footer Classes
 *
 *****/
 
/*------------------------------------*\
    #Mixins
\*------------------------------------*/

var ComponentStateMixin = {
  getInitialState: function() {
    return { close: false };
  },
  handleClick: function(event) {
    this.setState({ close: !this.state.close });
  }
};

/*------------------------------------*\
    #Components
\*------------------------------------*/

var OverlayNav = React.createClass({
  render: function() {
    return (
          <div className="visible overlay animated fadeIn">
                <nav>
                    <div className="menu animated fadeInDown">
                        <img className="logo-overlay" alt="Penn Crest" src="/techblog/static/img/upenn_crest_overlay.png"/>
                    </div>
                    <div className="menu animated fadeInDown">
                        <a href="/techblog">Home</a>
                    </div>
                    <div className="menu animated fadeInDown">
                        <a href="/techblog/team">About</a>
                    </div>
                    <div className="menu animated fadeInDown">
                        <a href="https://apps.wharton.upenn.edu/techblog/feed/latest/">RSS Feed</a>
                    </div>
                    <div className="menu animated fadeInDown">
                        <a href="https://github.com/wharton">Github</a>
                    </div>
                    <div className="menu animated fadeInDown">
                        <a href="http://www.wharton.upenn.edu">Wharton</a>
                    </div>
                    <div className="menu animated fadeInDown">
                        <a href="http://www.upenn.edu">UPenn</a>
                    </div>
                </nav>
          </div>
    );
  }
});



var BlogButton = React.createClass({
  mixins: [ ComponentStateMixin ],
  render: function() {
    var text = this.state.close ? 'navOpen fa' : 'navClose fa';
    var over = this.state.close ? 'visible overlay animated fadeIn' : 'invisible';
    var menu = this.state.close ? 'menu animated fadeInDown' : 'invisible';
    var show_hide = this.state.close ? 'show' : 'hide';
    return (
     <div id="navWrap" onClick={this.handleClick}>
        <nav className="nav nav-blog pop blog-post" >
              <span className={text}></span>
        </nav>
        <div className={show_hide}>
             <OverlayNav />
         </div>
      </div>
    );
  }
});

ReactDOM.render(
  <BlogButton />,
  document.getElementById('nav-blog--react')
);

