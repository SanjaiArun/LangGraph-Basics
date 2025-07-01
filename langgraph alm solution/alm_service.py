from abc import ABC, abstractmethod

class ALMService(ABC):
    @abstractmethod
    def create_issue(self, *args,**kwargs):
        """Create a new issue in the ALM system."""
        pass
    @abstractmethod
    def update_issue(self, *args,**kwargs):
        """Update an existing issue in the ALM system."""
        pass
    @abstractmethod
    def get_issue(self, *args,**kwargs):
        """Retrieve an issue from the ALM system."""
        pass
    @abstractmethod
    def delete_issue(self, *args,**kwargs):
        """Delete an issue from the ALM system."""
        pass