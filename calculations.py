from datetime import date

class Calculations:
    def __init__(self, principal, interest_rate, duration_months, start_date=date.today()):
        self.principal = principal
        self.interest_rate = interest_rate
        self.duration_months = duration_months
        self.start_date = start_date
        self.months_since_start = start_date - date.today()
        print(f"Months since start: {self.months_since_start}")
    
    def balance_at_month(self, current_month):
        balance = self.principal
        duration_months = self.duration_months
        temp = ((1+self.interest_rate/12)**duration_months)-(1+self.interest_rate/12)**(current_month)
        temp2 = ((1+self.interest_rate/12)**duration_months) - 1
        return balance*(temp/temp2)
    
    def monthly_payment(self):
        balance = self.principal
        rate = self.interest_rate
        duration = self.duration_months
        temp = ((1+rate/12)**duration)*(rate/12)
        temp2 = ((1+rate/12)**duration)-1
        return balance*(temp/temp2)
    
    def cumulative_interest(self, current_month):
        rate = self.interest_rate
        duration = self.duration_months
        balance = self.principal
        monthlyPayment = self.monthly_payment()
        totalPaid = monthlyPayment*current_month
        remainingBalance = self.balance_at_month(current_month)
        principalRepaid = balance - remainingBalance
        return totalPaid - principalRepaid
    

    # Method to generate the amortization schedule and return it as a list of dictionaries
    def amortization_schedule(self, extra_payments=None):
        if extra_payments is None:
            extra_payments = {}  # Initialize with an empty dictionary if no extra payments provided

        schedule = []
        temp_balance = self.principal
        mnth_payment = self.monthly_payment()
        rate = self.interest_rate / 12  # Monthly interest rate
        month = 1

        while temp_balance > 0:
            # Calculate the interest for the current month
            interest = temp_balance * rate
            principal_payment = mnth_payment - interest

            # Check if there's an extra payment for this month
            extra_payment = extra_payments.get(month, 0)
            principal_payment += extra_payment

            # If the balance is less than the payment + extra payment, adjust the last payment
            if temp_balance < principal_payment:
                principal_payment = temp_balance
                mnth_payment = temp_balance + interest

            
            
            # Update the balance
            temp_balance -= principal_payment

            

            # Add the details to the schedule list as a dictionary
            schedule.append({
                'Month': month,
                'Payment': mnth_payment,
                'Principal Payment': principal_payment,
                'Interest Payment': interest,
                'Extra Payment': extra_payment,
                'Remaining Balance': temp_balance
            })

            # Move to the next month
            month += 1

        return schedule

    # Method to print the amortization schedule
    def print_amortization_schedule(self, schedule_print=None):
        # Add test dictionary for extra payments
        extra_payments_dict = {6: 1000, 7: 500, 8: 100, 10: 3000, 20: 10_000}

        # Get the amortization schedules
        

        if schedule_print is None:
            schedule_print = self.amortization_schedule()

        schedule_print = self.amortization_schedule(extra_payments=extra_payments_dict)  # With extra payments

        # Print header
        print(f"{'Month':<10}{'Payment':<15}{'Principal':<15}{'Interest':<15}{'Balance':<15}{'Extra Payment':<15}")
        print("-" * 90)
        
        # Loop through the schedule and print each entry
        for entry in schedule_print:
            if entry['Extra Payment'] > 0:
                print(f"{entry['Month']:<10}{entry['Payment']:<15.2f}{entry['Principal Payment']:<15.2f}{entry['Interest Payment']:<15.2f}{entry['Remaining Balance']:<15.2f} {entry['Extra Payment']:<15}")

            else:
                print(f"{entry['Month']:<10}{entry['Payment']:<15.2f}{entry['Principal Payment']:<15.2f}{entry['Interest Payment']:<15.2f}{entry['Remaining Balance']:<15.2f}")
        return schedule_print
    

    # Method to calculate the total interest paid over the life of the loan
    def total_interest_paid(self):
        schedule = self.amortization_schedule()
        total_interest = 0
        for entry in schedule:
            total_interest += entry['Interest Payment']
        return total_interest


    def plot_balance(self):
        # Add test dictionary for extra payments
        extra_payments_dict = {6: 1000, 7: 500, 8: 100, 10: 3000, 20: 10_000}

        # Get the amortization schedules
        schedule = self.amortization_schedule()  # Without extra payments
        extra_payments_schedule = self.amortization_schedule(extra_payments=extra_payments_dict)  # With extra payments

        # Extract 'Month' and 'Remaining Balance' into lists for both schedules
        months = [entry['Month'] for entry in schedule]
        remaining_balances = [entry['Remaining Balance'] for entry in schedule]

        months_extra = [entry['Month'] for entry in extra_payments_schedule]
        remaining_balances_extra = [entry['Remaining Balance'] for entry in extra_payments_schedule]

        # Plot the remaining balances for both schedules
        plt.plot(months, remaining_balances, label="Remaining Balance")
        plt.plot(months_extra, remaining_balances_extra, label="Remaining Balance with Extra Payments")

        # Set for tracking annotated months
        annotated_months = set()

        # Add in the annotations for the extra payments, but only for the first occurrence
        for entry in extra_payments_schedule:
            if entry['Extra Payment'] > 0 and entry['Month'] not in annotated_months:
                plt.annotate(f"${entry['Extra Payment']} - {entry['Month']}", (entry['Month'], entry['Remaining Balance']), textcoords="offset points", xytext=(50, 10), ha='center', arrowprops=dict(arrowstyle="->", lw=1.5))
                annotated_months.add(entry['Month'])  # Mark this month as annotated

        # Add labels, title, and legend
        plt.xlabel('Month')
        plt.ylabel('Remaining Balance')
        plt.title('Remaining Balance Over Time')
        plt.legend()

        # Show the plot
        plt.show()


    def extra_monthly_payment(self, extra_payment, month_of_payment):
        schedule = self.amortization_schedule()
        new_schedule = []