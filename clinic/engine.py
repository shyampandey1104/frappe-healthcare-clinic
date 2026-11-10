"""Outpatient Clinic & Healthcare OPD Engine for Frappe Framework."""

from typing import Dict, Any, List, Optional
from datetime import datetime
from pydantic import BaseModel


class Patient(BaseModel):
    patient_id: str
    name: str
    age: int
    gender: str
    phone: str
    blood_group: Optional[str] = None


class PrescriptionItem(BaseModel):
    medicine_name: str
    dosage: str  # 1-0-1 after food
    duration_days: int
    quantity: int


class ConsultationRecord(BaseModel):
    encounter_id: str
    patient_id: str
    doctor_name: str
    symptoms: List[str]
    diagnosis: str
    vitals: Dict[str, str]  # bp, pulse, temperature
    prescriptions: List[PrescriptionItem] = []
    consultation_fee: float = 500.0


class ClinicEngine:
    """Manages clinic patient encounters, e-prescriptions, and billing."""

    def __init__(self):
        self.patients: Dict[str, Patient] = {}
        self.encounters: Dict[str, ConsultationRecord] = {}

    def register_patient(self, patient: Patient) -> Patient:
        self.patients[patient.patient_id] = patient
        return patient

    def record_consultation(self, encounter: ConsultationRecord) -> ConsultationRecord:
        if encounter.patient_id not in self.patients:
            raise ValueError("Patient not registered in clinic database")
        self.encounters[encounter.encounter_id] = encounter
        return encounter

    def generate_encounter_summary(self, encounter_id: str) -> Dict[str, Any]:
        if encounter_id not in self.encounters:
            raise ValueError("Encounter record not found")

        enc = self.encounters[encounter_id]
        pat = self.patients.get(enc.patient_id)

        return {
            "encounter_id": enc.encounter_id,
            "patient_name": pat.name if pat else "Unknown",
            "age_gender": f"{pat.age} / {pat.gender}" if pat else "",
            "doctor": enc.doctor_name,
            "diagnosis": enc.diagnosis,
            "vitals": enc.vitals,
            "medications_count": len(enc.prescriptions),
            "consultation_fee": enc.consultation_fee,
            "status": "Completed",
        }
