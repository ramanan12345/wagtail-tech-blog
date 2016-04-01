'use strict';
require('es6-promise').polyfill();

// Load required files that aren't auto-loaded by
// gulp-load-plugins (see below)
var argv            = require('yargs').argv,
    fs              = require('fs'),
    gulp            = require('gulp'),
    merge           = require('merge-stream'),
    minifyCss       = require('gulp-minify-css'),
    path            = require('path');

// Browserify specific
var babelify = require('babelify'),
    browserify = require('browserify'),
    source = require('vinyl-source-stream');

// This will load any gulp plugins automatically that
// have this format ('gulp-pluginName' [can only have one dash])
// The plugin can used as $.pluginName 
var $ = require('gulp-load-plugins')();

// Paths
var javascriptsPath     = 'static_dev/javascripts',
    sassPath            = 'static_dev/scss';

// Get Folder Function (from paths)
function getFolders(dir) {
    return fs.readdirSync(dir)
        .filter(function(file) {
            return fs.statSync(path.join(dir, file)).isDirectory();
        });
}


// Javascript task
// If coding in Javascript, this will concat, jshint, and uglify
// Copies files to the static javascript directory
gulp.task('scripts-javascript', function() {
    var folders = getFolders(javascriptsPath);
    var tasks   = folders.map(function(folder) {
        return gulp.src(
        [
            'static_dev/javascripts/' + folder + '/caosblog.js',
        ], { base: 'static_dev/javascripts/' + folder })
            // concat files
            .pipe($.concat(folder + '.js'))
            // Check integrity
            .pipe($.jshint())
            // Remove whitespace and uglify
            .pipe($.uglify())
            // Rename the file
            .pipe($.rename(folder + '.min.js'))
            // Copy it to static folder
            .pipe(gulp.dest('static/javascripts'))
    });

    return merge(tasks);
});

// Browserify task
gulp.task('scripts-browserify', function() {
    var folders = getFolders(javascriptsPath);

    var tasks = folders.map(function(folder) {
        return browserify({
            entries: ['./static_dev/javascripts/' + folder + '/caosblog.js'],
            debug: true
        })
            .transform(babelify,  { presets: ['es2015', 'react'] })
            .bundle()
                .pipe(source(folder + '.js'))
                //.pipe($.uglify())
                .pipe($.rename(folder + '.min.js'))
                .pipe(gulp.dest('./static/javascripts/'));
    });

    return merge(tasks);
});

// SASS Task
// Compiles, concats, minifies, and versions scss files
gulp.task('styles-sass', function() {
    var folders = getFolders(sassPath);
    var tasks   = folders.map(function(folder) {
        return gulp.src(['static_dev/scss/' + folder + '/*.scss'], 
            { base: 'static_dev/scss/' + folder }
        )
            // Compile to CSS
            .pipe($.sass({
                outputStyle: 'nested',
                precision: 10,
                includePaths: ['.'],
                onError: console.error.bind(console, 'Sass error:')
            }))
            // Concat files
            .pipe($.concat(folder + '.css'))
            // Minify CSS
            .pipe(minifyCss({ compatibility: 'ie9', rebase: false }))
            // Post CSS processor
            .pipe($.postcss([
                require('autoprefixer')({ browsers: ['last 1 version'] })
            ]))
            // Rename the file
            .pipe($.rename(folder + '.min.css'))
            // Copy it to static folder
            .pipe(gulp.dest('static/stylesheets'))
    });

    return merge(tasks);
});

gulp.task('build', ['styles-sass', 'scripts-browserify'])
