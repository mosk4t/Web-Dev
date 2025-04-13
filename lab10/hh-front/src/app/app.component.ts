import { Component, OnInit, inject } from '@angular/core'; 
import { CommonModule } from '@angular/common'; 
import { ApiService } from './services/api.service';
import { Company } from './models/company';
import { Vacancy } from './models/vacancy';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule], 
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'HeadHunter (Lab 10)';
  companies: Company[] = [];
  vacancies: Vacancy[] = [];
  selectedCompany: Company | null = null;
  loadingCompanies = false;
  loadingVacancies = false;
  errorCompanies: string | null = null;
  errorVacancies: string | null = null;

 
  private apiService = inject(ApiService);

  ngOnInit(): void {
    this.loadCompanies(); 
  }

  loadCompanies(): void {
    this.loadingCompanies = true;
    this.errorCompanies = null;
    this.selectedCompany = null; 
    this.vacancies = []; 

    this.apiService.getCompanies().subscribe({
      next: (data) => {
        this.companies = data;
        this.loadingCompanies = false;
        console.log('Companies loaded:', this.companies);
      },
      error: (err) => {
        console.error('Error loading companies:', err);
        this.errorCompanies = 'Failed to load companies. Is the backend running?';
        this.loadingCompanies = false;
      }
    });
  }

  selectCompany(company: Company): void {
    if (this.selectedCompany === company) {
      return; 
    }

    this.selectedCompany = company;
    this.vacancies = []; 
    this.loadingVacancies = true;
    this.errorVacancies = null;
    console.log('Selected company:', this.selectedCompany);

    this.apiService.getCompanyVacancies(company.id).subscribe({
      next: (data) => {
        this.vacancies = data;
        this.loadingVacancies = false;
        console.log('Vacancies loaded:', this.vacancies);
      },
      error: (err) => {
        console.error(`Error loading vacancies for company ${company.id}:`, err);
        this.errorVacancies = `Failed to load vacancies for ${company.name}.`;
        this.loadingVacancies = false;
      }
    });
  }
}