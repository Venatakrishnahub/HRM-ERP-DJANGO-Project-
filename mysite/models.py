# models.py

from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    dob = models.DateField()
    doj = models.DateField()
    employment_type = models.CharField(max_length=50, choices=[('intern', 'Intern'), ('contract', 'Contract'), ('full-time', 'Full-time'), ('part-time', 'Part-time'), ('probation', 'Probation')])
    # job_status = models.CharField(max_length=50, choices=[('direct', 'Direct'), ('contract', 'Contract'), ('full-time', 'Full-time'), ('part-time', 'Part-time'), ('partial', 'Partial'), ('casual', 'Casual'), ('temporary-agency', 'Temporary Agency')])
    offer_date = models.DateField(blank=True, null=True)
    confirmation_date = models.DateField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)
    notice_days = models.IntegerField(blank=True, null=True)
    retirement_date = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    reports_to = models.CharField(max_length=100, blank=True, null=True)
    leave_policy = models.CharField(max_length=100, blank=True, null=True)
    holiday_list = models.CharField(max_length=100, blank=True, null=True)
    salary_payment_mode = models.CharField(max_length=50, choices=[('bank', 'Bank'), ('cheque', 'Cheque'), ('cash', 'Cash')])
    salary_amount=models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)
    current_address = models.TextField()
    permanent_address = models.TextField()
    personal_email = models.EmailField()
    company_email = models.EmailField(blank=True, null=True)
    preferred_email = models.CharField(max_length=50, choices=[('company', 'Company Email'), ('personal', 'Personal Email')])
    parent_name = models.CharField(max_length=100, blank=True, null=True)
    parent_occupation = models.CharField(max_length=100, blank=True, null=True)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_occupation = models.CharField(max_length=100, blank=True, null=True)
    children = models.CharField(max_length=100, blank=True, null=True)
    passport_details = models.CharField(max_length=100, blank=True, null=True)
    health_details = models.TextField(blank=True, null=True)
    exit_status = models.CharField(max_length=20, choices=[('employed', 'Employed'), ('left', 'Left')], blank=True, null=True)
    relieving_date = models.DateField(blank=True, null=True)
    resignation = models.CharField(max_length=100, blank=True, null=True)
    exit_interview = models.CharField(max_length=100, blank=True, null=True)
    leave_encashment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

