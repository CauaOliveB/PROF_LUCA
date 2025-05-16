from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select    

from models.instructor_models import InstructorModel
from schemas.instructor_schemas import InstructorSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=InstructorSchema)
async def psot_instructor(instructor: InstructorSchema, db: AsyncSession = Depends(get_session)):
    new_instructor = InstructorModel(name = instructor.name, age=instructor.age,subject= instructor.subject, photo=instructor.photo )
    
    db.add(new_instructor)
    
    await db.commit()
    
    return new_instructor

@ router.get("/", response_model=List[InstructorSchema])
async def get_instructors(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstructorModel)
        result = await session.execute(query)
        
        instructors: List[InstructorModel] = result.scalar().all()
        
        return instructors
    
@router.get("/{instructor_id}", response_model = InstructorSchema)
async def get_instructor(instructor_id : int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstructorModel).filter(InstructorModel.id == instructor_id)
        
        result = await session.execute(query)
        
        instructor = result.scalar_one_or_none()
        
        if instructor:
            return instructor
        else:
            raise HTTPException(detail="Instructor Not Founded",
                                status_code=status.HTTP_404_NOT_FOUND)

@router.put("/{instructor_id}", response_model = InstructorSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_instructor(instructor_id: int, instructor: InstructorSchema, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstructorModel).filter(InstructorModel.id == instructor_id)
        
        result = await session.execute(query)
        
        instructor_up = result.scalar_one_or_none()
        
        if instructor_up:
            instructor_up.name = instructor.name
            instructor_up.age = instructor.age
            instructor_up.subject = instructor.subject
            instructor_up.photo = instructor.photo
            
            await session.commit()
            return instructor_up
        
        else:
            raise HTTPException(detail="Instructor Not Founded",
                                status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{instrutor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_instructor(instructor_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstructorModel).filter(InstructorModel.id == instructor_id)
        
        result = await session.execute(query)
        
        instructor_del = result.scalar_one_or_none()
        
        if instructor_del:
            await session.delete(instructor_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(detail="Instructor Not Founded",status_code=status.HTTP_404_NOT_FOUND)
