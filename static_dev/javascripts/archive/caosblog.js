var BlogPosts = React.createClass({
  render: function() {
    var articles = this.props.posts;
    if (articles) {
      return (
        <div>
        <div className="timeline-month">April 2015</div>
        <div className="timeline-wrapper">
          {articles.map(function(article, index) {
            var hostname = location.origin,
                img_url = article.img_url,
                article_url = hostname + article.url;
            return (
                  <div className="timeline" key={index}>
                      <div className="timeline__info">
                        <i className="fa fa-caret-right"></i>
                        <i className="fa fa-caret-left"></i>
                        <ul>
                          <li key={index}><img className="time-img" key={index} src={img_url} /></li>
                          <li>{article.category.join(',')}</li>
                          <li>{article.author}</li>
                          <li>{article.date}</li>
                        </ul>
                      </div>
                  </div>
            );  
          })}
        </div>
        </div>
      );
    } else {
      return <div>No Posts</div>;
    }
  }
});

var ArchiveMonth = React.createClass({
  render: function() {
    var monthNames = ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ];

    var available_dates = this.props.dates.map(function(date) {
      var date_obj = new Date(date.date);

      return monthNames[date_obj.getMonth()];
    });
    var trim_date = _.uniq(available_dates),
        self = this;

    if (available_dates) {
      return (
        <div>
            {trim_date.map(function(date, index) {
              return <div className="month" key={index} onClick={self.props.updateByMonth}>{date}</div>
            })}
        </div>
      );
    } else {
      return false;
    }
  }
});

var ArchiveYear = React.createClass({
  render: function() {
    return (
      <div>
        <ul className="year">
          <li onClick={this.props.updateByYear}>2016</li>
          <li onClick={this.props.updateByYear}>2015</li>
          <li onClick={this.props.updateByYear}>2014</li>
          <li onClick={this.props.updateByYear}>2013</li>
        </ul>
      </div>
    );
  }
});

var ArchiveApp = React.createClass({
  getInitialState: function() {
    return {
      articles: false,
      filter_settings: null,
      errors: null
    };
  },
  componentDidMount: function() {
    var self = this,
        hostname = location.origin,
        api_uri = hostname + "/techblog/api/blog/live_blogs/";

    $.get(api_uri)
    .done(function(posts) {
      self.setState({articles: posts});
    })
    .fail(function() {
      msg = 'An Error has occurred. Please try again later'
      self.setState({errors: msg});
    });
  },
  month_selected: function(evt) {
    var sel_month = evt.target.innerHTML,
        monthNames = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"
        ];
    
    var filter = this.state.filter_settings ? this.state.filter_settings : this.state.articles; 
    var sel_posts = _.filter(filter, function(obj) {
      var month_obj = new Date(obj.date),
          month_index = monthNames.indexOf(sel_month);

      if (month_index === month_obj.getMonth()) {
        return obj;
      }
    }); 

    this.setState({filter_settings: sel_posts});
  },
  year_selected: function(evt) {
    var sel_year = $(evt.target).text();
    var filter_year = _.filter(this.state.articles, function(dates) {
      if (dates.date.indexOf(sel_year) > -1) {
        return dates;
      }
    });

    this.setState({filter_settings: filter_year});
  },
  render: function() {
    var yearSelector = <ArchiveYear updateByYear={this.year_selected} />;

    if (this.state.errors) {
      var errorPanel = this.state.errors.msg;
    }
    else if (this.state.filter_settings) {
      if (this.state.filter_settings.length > 0) {
        var monthSelector = <ArchiveMonth dates={this.state.filter_settings} updateByMonth={this.month_selected} />;
        var blogPosts = <BlogPosts posts={this.state.filter_settings} />;
      }
      else
        var noResults = "No Results";
    }
    else if (this.state.articles) {
      var monthSelector = <ArchiveMonth dates={this.state.articles} updateByMonth={this.month_selected} />;
      var blogPosts = <BlogPosts posts={this.state.articles} />;
    }
    return (
      <div className="article-wrap">
        {yearSelector} 
        {monthSelector}
        {blogPosts}
        {noResults}
        {errorPanel}
      </div>
    );
  }
});

ReactDOM.render(
  <ArchiveApp />,
  document.getElementById("main")  
);
