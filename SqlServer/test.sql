IF EXISTS (
		SELECT *
		FROM sys.objects
		WHERE object_id = OBJECT_ID(N'dbo.[CarePlanPatternFact]')
			AND type IN (N'U')
		)
	DROP TABLE dbo.[CarePlanPatternFact]
GO



-- Sabarish Hariraj 6/2/2015  DR6099 Initial Version --


