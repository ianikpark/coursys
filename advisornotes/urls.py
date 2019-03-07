from django.conf.urls import url
from courselib.urlparts import UNIT_COURSE_SLUG, NOTE_ID, SEMESTER, COURSE_SLUG, ARTIFACT_SLUG, USERID_OR_EMPLID, \
    NONSTUDENT_SLUG, UNIT_SLUG, SLUG_RE
import advisornotes.views as advisornotes_views

CATEGORY_SLUG = '(?P<category_slug>' + SLUG_RE + ')'
VISIT_SLUG = '(?P<visit_slug>' + SLUG_RE + ')'


advisornotes_patterns = [ # prefix /advising/
    url(r'^$', advisornotes_views.advising, name='advising'),
    #url(r'^new_notes/$', advisornotes_views.rest_notes, name='rest_notes'),
    url(r'^hide_note$', advisornotes_views.hide_note, name='hide_note'),
    url(r'^note_search$', advisornotes_views.note_search, name='note_search'),
    url(r'^download_notes$', advisornotes_views.download_notes_summary, name='download_notes'),
    url(r'^artifact_search$', advisornotes_views.artifact_search, name='artifact_search'),
    url(r'^sims_search$', advisornotes_views.sims_search, name='sims_search'),
    url(r'^sims_add$', advisornotes_views.sims_add_person, name='sims_add_person'),
    url(r'^visits$', advisornotes_views.all_visits, name='all_visits'),
    url(r'^my_visits$', advisornotes_views.my_visits, name='my_visits'),

    url(r'^categories$', advisornotes_views.manage_categories, name='manage_categories'),
    url(r'^categories/add$', advisornotes_views.add_category, name='add_category'),
    url(r'^categories/' + CATEGORY_SLUG + '/delete/$', advisornotes_views.delete_category, name='delete_category'),
    url(r'^categories/' + CATEGORY_SLUG + '/edit/$', advisornotes_views.edit_category, name='edit_category'),

    url(r'^courses/$', advisornotes_views.view_courses, name='view_courses'),
    url(r'^courses/' + UNIT_COURSE_SLUG + '/new$', advisornotes_views.new_artifact_note, name='new_artifact_note'),
    url(r'^courses/' + UNIT_COURSE_SLUG + '/moreinfo$', advisornotes_views.course_more_info, name='course_more_info'),
    url(r'^courses/' + UNIT_COURSE_SLUG + '/' + NOTE_ID + '/edit$', advisornotes_views.edit_artifact_note, name='edit_artifact_note'),
    url(r'^courses/' + UNIT_COURSE_SLUG + '/$', advisornotes_views.view_course_notes, name='view_course_notes'),
    url(r'^offerings/$', advisornotes_views.view_course_offerings, name='view_course_offerings'),
    url(r'^offerings/semesters$', advisornotes_views.view_all_semesters, name='view_all_semesters'),
    url(r'^offerings/' + SEMESTER + '$', advisornotes_views.view_course_offerings, name='view_course_offerings'),
    url(r'^offerings/' + COURSE_SLUG + '/new$', advisornotes_views.new_artifact_note, name='new_artifact_note'),
    url(r'^offerings/' + COURSE_SLUG + '/$', advisornotes_views.view_offering_notes, name='view_offering_notes'),
    url(r'^offerings/' + COURSE_SLUG + '/' + NOTE_ID + '/edit$', advisornotes_views.edit_artifact_note, name='edit_artifact_note'),
    url(r'^artifacts/$', advisornotes_views.view_artifacts, name='view_artifacts'),
    url(r'^artifacts/' + ARTIFACT_SLUG + '/new$', advisornotes_views.new_artifact_note, name='new_artifact_note'),
    url(r'^artifacts/' + ARTIFACT_SLUG + '/$', advisornotes_views.view_artifact_notes, name='view_artifact_notes'),
    url(r'^artifacts/' + ARTIFACT_SLUG + '/' + NOTE_ID + '/edit$', advisornotes_views.edit_artifact_note, name='edit_artifact_note'),
    url(r'^new_artifact$', advisornotes_views.new_artifact, name='new_artifact'),
    url(r'^artifacts/' + ARTIFACT_SLUG + '/edit$', advisornotes_views.edit_artifact, name='edit_artifact'),
    url(r'^artifacts/' + NOTE_ID + '/file', advisornotes_views.download_artifact_file, name='download_artifact_file'),

    url(r'^students/' + USERID_OR_EMPLID + '/new$', advisornotes_views.new_note, name='new_note'),
    url(r'^students/' + USERID_OR_EMPLID + '/$', advisornotes_views.student_notes, name='student_notes'),
    url(r'^students/' + NONSTUDENT_SLUG + '/$', advisornotes_views.student_notes, name='student_notes'),
    url(r'^students/' + NONSTUDENT_SLUG + '/merge$', advisornotes_views.merge_nonstudent, name='merge_nonstudent'),
    url(r'^students/' + USERID_OR_EMPLID + '/' + NOTE_ID + '/file', advisornotes_views.download_file, name='download_file'),
    url(r'^students/' + USERID_OR_EMPLID + '/moreinfo$', advisornotes_views.student_more_info, name='student_more_info'),
    url(r'^students/' + USERID_OR_EMPLID + '/moreinfo_short$', advisornotes_views.student_more_info_short,
        name='student_more_info_short'),
    url(r'^students/' + USERID_OR_EMPLID + '/courses$', advisornotes_views.student_courses, name='student_courses'),
    url(r'^students/' + USERID_OR_EMPLID + '/visited/' + UNIT_SLUG, advisornotes_views.record_advisor_visit,
        name='record_advisor_visit'),
    url(r'^students/' + VISIT_SLUG + '/edit$', advisornotes_views.edit_visit, name='edit_visit'),
    url(r'^students/' + VISIT_SLUG + '/view$', advisornotes_views.view_visit, name='view_visit'),
    url(r'^students/' + VISIT_SLUG + '/end_mine$', advisornotes_views.end_visit_mine, name='end_visit_mine'),
    url(r'^students/' + VISIT_SLUG + '/end_admin$', advisornotes_views.end_visit_admin, name='end_visit_admin'),
    url(r'^students/' + USERID_OR_EMPLID + '/courses-data$', advisornotes_views.student_courses_data, name='student_courses_data'),
    url(r'^students/' + USERID_OR_EMPLID + '/courses-download$', advisornotes_views.student_courses_download, name='student_courses_download'),
    url(r'^students/' + USERID_OR_EMPLID + '/transfers-data$', advisornotes_views.student_transfers_data, name='student_transfers_data'),
    url(r'^students/' + USERID_OR_EMPLID + '/transfers$', advisornotes_views.student_transfers, name='student_transfers'),
    url(r'^students/' + USERID_OR_EMPLID + '/transfers-download$', advisornotes_views.student_transfers_download, name='student_transfers_download'),

    url(r'^new_prospective_student', advisornotes_views.new_nonstudent, name='new_nonstudent'),
    #url(r'^problems/$', advisornotes_views.view_problems, name='view_problems'),
    #url(r'^problems/resolved/$', advisornotes_views.view_resolved_problems, name='view_resolved_problems'),
    #url(r'^problems/(?P<prob_id>\d+)/$', advisornotes_views.edit_problem, name='edit_problem'),
]
