# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Education",
    "version": "12.0.7.0.0",
    "category": "Education",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "depends": [
        "base",
        "resource",
        "hr",
        "partner_firstname",
        "partner_second_lastname",
        "partner_contact_birthdate",
        "report_xlsx",
    ],
    "data": [
        "security/education_groups.xml",
        "security/education_rules.xml",
        "security/ir.model.access.csv",
        "data/education_employee_data.xml",
        "reports/education_group_report_view.xml",
        "reports/education_group_teacher_report_view.xml",
        "reports/education_group_student_report_view.xml",
        "reports/education_group_student_timetable_report_view.xml",
        "reports/education_group_teacher_timetable_report_view.xml",
        "reports/education_group_xlsx_report.xml",
        "views/res_partner_view.xml",
        "views/education_academic_year_view.xml",
        "views/education_academic_year_evaluation_view.xml",
        "views/education_activity_type_view.xml",
        "views/education_classroom_view.xml",
        "views/education_contract_type_view.xml",
        "views/education_course_view.xml",
        "views/education_designation_level_view.xml",
        "views/education_field_view.xml",
        "views/education_group_view.xml",
        "views/education_group_type_view.xml",
        "views/education_idtype_view.xml",
        "views/education_language_view.xml",
        "views/education_level_view.xml",
        "views/education_level_workday_type_view.xml",
        "views/education_model_view.xml",
        "views/education_plan_view.xml",
        "views/education_position_view.xml",
        "views/education_schedule_view.xml",
        "views/education_section_view.xml",
        "views/education_shift_view.xml",
        "views/education_subject_view.xml",
        "views/education_subject_center_view.xml",
        "views/education_subject_type_view.xml",
        "views/education_task_type_view.xml",
        "views/education_work_reason_view.xml",
        "views/education_workday_type_view.xml",
        "views/hr_employee_view.xml",
        "views/res_lang_view.xml",
        "views/report_education_group.xml",
        "views/report_education_schedule.xml",
        "views/report_employee_timetable.xml",
        "views/report_group_timetable.xml",
        "views/report_student_timetable.xml",
        "wizards/education_group_next_year_view.xml",
        "views/education_menu_view.xml",
    ],
    "installable": True,
    "application": True,
}
