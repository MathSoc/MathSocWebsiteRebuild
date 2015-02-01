/**
 * Exam list of form:
 * [{'code': SUBJECT_CODE,
 *   'courses': [COURSE_CODE, ...]},
 *  ...]
 */

var subjects = [];

var current_subject = "";
var current_course = "";


/**
 * @summary: Populates a <select> with data from the options
 *
 * @args:
 *      selector {String}: for the DOM (jQuery format)
 *      options [Array]: to populate the <select> with
 */
function populateSelect(selector, options) {
    var option_div = $(selector);
    $.each(options, function() {
        option_div.append($("<option />").val(this).text(this));
    });
}

function subjectChange(changed_to) {
    if (changed_to === "") {
        $("#code-selection").attr("disabled", true);
    }
    else {
        $("#code-selection").attr("disabled", false);
        
        var course_codes = getCodes(changed_to);
        $("#code-selection").children().remove();
        populateSelect("#code-selection", course_codes);
    }
}

function codeChange(changed_to) {
    displayExam(current_subject, current_course);
}


function displayExam(subject, course) {
    var fetch_promise = fetchExam(subject, course);

    fetch_promise.done(function (exam_data) {
        // do stuff to display exam here
    });
}

function fetchExam(subject, course) {
    var promise = $.ajax({
        'url': '/resources/exambank/exams',
        'method': 'GET',
        'data': {
            'subject': subject,
            'course': course
        }
    });
    return promise;
}

function getCodes(subject) {
    var subject_obj = subjects.filter(function(sub) {
        return sub.code === subject;
    })[0];
    return subject_obj.courses;
}

function fetchCourseList() {
    var promise = $.ajax({
        'url': '/resources/exambank/courses',
        'method': 'GET'
    });

    promise.done(function(data) {
        subjects = data;
        var subject_list = subjects.map(function(subject) {
            return subject.code;
        });
        populateSelect("#subject-list", subject_list);
    });
}

$(function() {
    fetchCourseList();
});