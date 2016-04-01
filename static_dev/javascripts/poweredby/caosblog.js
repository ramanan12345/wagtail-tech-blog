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

/*------------------------------------*\
    #Footer Classes
\*------------------------------------*/

var PoweredBy = React.createClass({
  getInitialState: function() {
    return {hide: false};
  },
  handleClick: function(event) {
    this.setState({hide: !this.state.hide});
  },
  render: function() {
    var click = this.state.hide ? 'hide-tech' : 'show-tech';
    var show_hide = this.state.hide ? 'show-tech pow': 'hide-tech pow';
    return (
      <div onClick={this.handleClick}>
        <div className={click}>
        	<div className="cogs"></div>
        </div>
        <div className={show_hide}>
            <div className="tech"></div>
            <div>
            <span className="tech__title">CAOS Stack:</span> Python, Django, REST, React.js, Gulp, SCSS, HTML5, CSS3
            </div>          
        </div>
      </div>
    );
  }
});

ReactDOM.render(
  <PoweredBy />,
  document.getElementById('powered_by')
);
