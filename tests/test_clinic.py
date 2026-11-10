"""Unit tests for ClinicEngine."""

from clinic.engine import ClinicEngine, Patient, ConsultationRecord, PrescriptionItem


def test_clinic_encounter_flow():
    engine = ClinicEngine()
    patient = Patient(patient_id="PAT-001", name="Suresh Gupta", age=45, gender="Male", phone="9821234567")
    engine.register_patient(patient)

    encounter = ConsultationRecord(
        encounter_id="ENC-2026-001",
        patient_id="PAT-001",
        doctor_name="Dr. Mehta, MD",
        symptoms=["Fever", "Cough"],
        diagnosis="Acute Bronchitis",
        vitals={"bp": "120/80", "pulse": "76", "temperature": "100.2 F"},
        prescriptions=[
            PrescriptionItem(medicine_name="Amoxicillin 500mg", dosage="1-0-1", duration_days=5, quantity=10),
            PrescriptionItem(medicine_name="Paracetamol 650mg", dosage="1-0-1", duration_days=3, quantity=6),
        ],
        consultation_fee=600.0,
    )
    engine.record_consultation(encounter)

    summary = engine.generate_encounter_summary("ENC-2026-001")
    assert summary["patient_name"] == "Suresh Gupta"
    assert summary["diagnosis"] == "Acute Bronchitis"
    assert summary["medications_count"] == 2
    assert summary["consultation_fee"] == 600.0
